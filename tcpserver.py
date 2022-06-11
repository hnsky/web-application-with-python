import socket


class TCPServer:
    """
    TCPを行うサーバーを表すクラス
    """

    def serve(self):
        """
        サーバーを起動する
        """

        print("==サーバを起動する===")

        try:

            # socketを生成
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            server_socket.bind(("localhost", 8080))
            server_socket.listen(5)

            print("===接続待ち===")
            (client_socket, address) = server_socket.accept()
            print(f"===接続完了 remote_address:{address} ===")

            # データを取得する
            request = client_socket.recv(4096)

            # 取得データをファイルに書き出す
            with open("server_recv.txt", "wb") as f:
                f.write(request)

            # 通信を終了する
            client_socket.close()

        finally:
            print("===サーバーを終了する")


if __name__ == "__main__":
    server = TCPServer()
    server.serve()
