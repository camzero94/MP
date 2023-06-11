import React from "react";
import { useContext, useState, useCallback, useEffect } from "react";
import ContextSocket from "../context/context-socketio";

function ComponentLayer() {

  const Socket = useContext(ContextSocket);
  const [message, setMessage] = useState([]);

  const onReceiveMessage2 = useCallback(
    (receivedMessage) => {
      const obj = JSON.parse(receivedMessage);
      const data_points = Object.entries(obj).map(([key, value]) => {
        return {
          id: key,
          ...value,
        };
      });
      console.log(data_points);
      setMessage(data_points);
    },
    [setMessage]
  );
  const onReceiveMessage = useCallback(
    (receivedMessage) => {
      const obj = JSON.parse(receivedMessage);
      setTimeout(5);
      const arr = Object.entries(obj).map((e) =>
        e.map((value) => {
          if (value["light voltage"] && value.temp) {
            return [value["light voltage"], value.temp];
          }
        })
      );
      console.log(arr[0][1], arr[1][1]);
      const globalArr = [];
      globalArr.push(arr[0][1]);
      globalArr.push(arr[1][1]);
      setMessage(globalArr);
    },
    [setMessage]
  );

  useEffect(() => {
    if (Socket != null) Socket.on("sendPic_message", onReceiveMessage2);
  }, [Socket]);

  return (
    <div>
      {message.map((data_point) => {
        return (
          <h1>
            <b>{data_point.id}</b> --- Light Voltage:{" "}
            {data_point["light voltage"]} Temp :{data_point["temp"]}
          </h1>
        );
      })}
    </div>
  );
}

export default ComponentLayer;
