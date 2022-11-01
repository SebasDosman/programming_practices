import React from "react";
import { TodoCounter } from "./Components/TodoCounter.js";
import { TodoSearch } from "./Components/TodoSearch.js";
import { TodoList } from "./Components/TodoList.js";
import { TodoItem } from "./Components/TodoItem.js";
import { CreateTodoButton } from "./Components/CreateTodoButton.js";
//import "./Todos.css";

const todos = [
  { text: "Tarea 1", completed: true },
  { text: "Tarea 2", completed: true },
  { text: "Tarea 3", completed: true },
];

function Todos() {
  return (
    <React.Fragment>
      <TodoCounter />
      <br/>
      <TodoSearch />

      <TodoList>
        {todos.map(todo => (
          <TodoItem
            key={ todo.text }
            text={ todo.text }
            completed={ todo.completed }
          />
        ))}
      </TodoList>

      <CreateTodoButton />
    </React.Fragment>
  );
}

export default Todos;