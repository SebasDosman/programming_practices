import React from "react";
import "../Css/TodoCounter.css"

function TodoCounter() {
  return (
    <React.Fragment>
      <h1 className="TittleTodoCounter">Lista De Tareas 💻</h1>
      <h3 className="TodoCounter">Has completado 2 de 3 tareas...</h3>
    </React.Fragment>
  );
}

export { TodoCounter };