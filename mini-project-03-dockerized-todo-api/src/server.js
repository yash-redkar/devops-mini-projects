const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

let todos = [
  {
    id: 1,
    title: "Learn Docker basics",
    completed: true
  },
  {
    id: 2,
    title: "Build Dockerized To-Do API",
    completed: false
  }
];

app.get("/", (req, res) => {
  res.json({
    message: "Dockerized To-Do API is running",
    endpoints: ["/health", "/todos"]
  });
});

app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
    service: "dockerized-todo-api",
    version: "1.0.0"
  });
});

app.get("/todos", (req, res) => {
  res.json({
    count: todos.length,
    data: todos
  });
});

app.get("/todos/:id", (req, res) => {
  const id = Number(req.params.id);
  const todo = todos.find((item) => item.id === id);

  if (!todo) {
    return res.status(404).json({
      message: "Todo not found"
    });
  }

  res.json(todo);
});

app.post("/todos", (req, res) => {
  const { title, completed } = req.body;

  if (!title) {
    return res.status(400).json({
      message: "Title is required"
    });
  }

  const newTodo = {
    id: todos.length + 1,
    title,
    completed: completed || false
  };

  todos.push(newTodo);

  res.status(201).json({
    message: "Todo created successfully",
    data: newTodo
  });
});

app.put("/todos/:id", (req, res) => {
  const id = Number(req.params.id);
  const todo = todos.find((item) => item.id === id);

  if (!todo) {
    return res.status(404).json({
      message: "Todo not found"
    });
  }

  const { title, completed } = req.body;

  if (title !== undefined) {
    todo.title = title;
  }

  if (completed !== undefined) {
    todo.completed = completed;
  }

  res.json({
    message: "Todo updated successfully",
    data: todo
  });
});

app.delete("/todos/:id", (req, res) => {
  const id = Number(req.params.id);
  const index = todos.findIndex((item) => item.id === id);

  if (index === -1) {
    return res.status(404).json({
      message: "Todo not found"
    });
  }

  const deletedTodo = todos.splice(index, 1);

  res.json({
    message: "Todo deleted successfully",
    data: deletedTodo[0]
  });
});

app.listen(PORT, () => {
  console.log(`To-Do API running on port ${PORT}`);
});
