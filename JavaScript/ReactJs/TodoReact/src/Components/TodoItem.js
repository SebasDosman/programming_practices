import React from "react";
import "../Css/TodoItem.css"

function TodoItem(props) {
  return (
    <div className="DivTodoItem">
      <li className="TodoItem">
        <span className={`Icon Icon-check ${ props.completed && 'Icon-check--active' }`}>
        ✓
        </span>
        <p className={`TodoItem-p ${ props.completed && 'TodoItem-p--complete' }`}>
          { props.text }
        </p>
        <span className="Icon Icon-delete">
        ✗
        </span>
      </li>
    </div>
  );
}

export { TodoItem };