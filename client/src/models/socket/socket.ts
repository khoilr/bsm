import { ManagerOptions, Socket, SocketOptions, io } from "socket.io-client";
import EventDisposer from "./event_disposer";


class ClientSocket {
    private socket: Socket;
    private disposers: Array<EventDisposer> = [];

    constructor(host: string, options: Partial<ManagerOptions & SocketOptions>) {
        this.socket = io(host, options);
        this.socket.on('disconnect', () => {
            // remove all listener
            for (const disposer of this.disposers) {
                this.socket.off(disposer.name, disposer.listener);
                console.info('Remove listener ' + disposer.name)
            }
            console.info("Disconnect socket with server!");
        })

        this.socket.on('connect', () => {
            console.info("Socket connected!")
        })
        this.socket.on('error', () => {
            console.error("Error when run socket")
        })
    }

    public addListener(event_name: string, listener: (...args: any[]) => void) {
        this.socket.on(event_name, listener);
        this.disposers.push({
            name: event_name,
            listener,
        });
    }
    public emit(event: string, ...args: any[]) {
        this.socket.emit(event, args);

    }
    public connect() {
        this.socket.connect();
    }

    public disconnect() {
        this.socket.disconnect();
    }
}

export default ClientSocket;