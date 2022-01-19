import { createContext, useEffect, useState } from "react";
import client from "socket.io-client";
const Context = createContext();

export function ContextSocketProvider({ children }) {
  const [Socket, setSocket] = useState(null);

  useEffect(() => {
    const SOCKET_URI = "ws://localhost:5000";
    const sock = client(SOCKET_URI);
    setSocket(sock);
    return () => {
      // cleanup;
    };
  }, []);

  return <Context.Provider value={Socket}>{children}</Context.Provider>;
}

export default Context;
