import { ContextSocketProvider } from "./context/context-socketio";
import ComponentLayer from "./components/data";

function App() {
  return (
    <ContextSocketProvider>
      <div className='"App"'>
        <ComponentLayer />
      </div>
    </ContextSocketProvider>
  );
}

export default App;
