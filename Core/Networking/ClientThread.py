import time
import json
from threading import *
from Logic.Player import Player
from Logic.Device import Device
from Utils.Helpers import Helpers
from Protocol.LogicLaserMessageFactory import packets
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from DataBase.DBManager import DB
def _(*args):
    for arg in args:
        print(arg, end=' ')
    print()


class ClientThread(Thread):
    def __init__(self, client, address):
        super().__init__()
        self.client = client
        self.address = address
        self.db = DB
        self.config = json.loads(open('config.json', 'r').read())
        self.device = Device(self.client)
        self.player = Player(self.device)


    def recvall(self, length: int):
        data = b''

        while len(data) < length:
            s = self.client.recv(length)

            if not s:
                _(f"{Helpers.red}ERROR while receiving data!")
                break

            data += s
        return data



    def run(self):
        self.db = self.db()
        try:
            last_packet = time.time()
            while True:
                header = self.client.recv(7)

                if len(header) > 0:

                    last_packet = time.time()

                    # Packet Info
                    packet_id = int.from_bytes(header[:2], 'big')
                    packet_length = int.from_bytes(header[2:5], 'big')
                    packet_data = self.recvall(packet_length)

                    if self.address[0] in self.config['BannedIPs']:
                        self.player.err_code = 11
                        LoginFailedMessage(self.client, self.player, 'Account banned!').send()


                    if packet_id in packets:
                        packet_name = packets[packet_id].__name__
                        _(f'{Helpers.blue}[CLIENT] PacketID: {packet_id}, Name: {packet_name} Length: {packet_length}')

                        message = packets[packet_id](self.client, self.player, packet_data)
                        message.decode()
                        message.process(self.db)

                        if packet_id == 10101:
                            Helpers.connected_clients["Clients"][str(self.player.ID)] = {"SocketInfo": self.client}

                    else:
                        _(f'{Helpers.cyan}[CLIENT] Unhandled Packet! ID: {packet_id}, Length: {packet_length}')

                if time.time() - last_packet > 10:
                    _(f"{Helpers.cyan}[DEBUG] Client disconnected! IP: {self.address[0]}")
                    self.client.close()
                    self.db.close()
                    _(f"{Helpers.cyan}[DEBUG] Client disconnected! IP: {self.address[0]}")
                    Helpers.connected_clients['ClientsCount'] -= 1
                    break


        except ConnectionAbortedError:
            _(f"{Helpers.cyan}[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1
        except ConnectionResetError:
            _(f"{Helpers.cyan}[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1
        except TimeoutError:
            _(f"{Helpers.cyan}[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1