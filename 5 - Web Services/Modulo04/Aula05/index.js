import express, { json, response } from "express";
import statusCode from "http-status-codes";

const app = express();

const PORT = process.env.PORT || 3000;

let users = [
  { id: 1, name: "Tomás", age: 22 },
  { id: 2, name: "Ribeiro", age: 33 },
  { id: 3, name: "Caldas", age: 33 },
];
app.use(express.json());
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});

app.get("/users", (req, resp) => {
  return resp.send(users);
});

app.post("/users", (req, resp) => {
  const newUser = req.body;
  users.push(newUser);

  return resp.status(statusCode.CREATED).send(newUser);
});

app.put("/users/:userId", (req, resp) => {
  const userId = req.params.userId;
  const attUser = req.body;
  attUser.id = userId;

  users = users.map((user) => {
    if (Number(userId) === user.id) {
      return attUser;
    }
    return user;
  });
  return resp.send(attUser);
});

app.delete("/users/:userId", (req, resp) => {
  const userId = req.params.userId;
  users = users.filter((user) => user.id !== Number(userId));
  return resp.status(statusCode.NO_CONTENT).send();
});
