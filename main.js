const app = [
  { name: "stephen", age: 23 },
  { name: "ron", age: 20 },
];

app.map((item) => {
  const { name, age } = item;
  console.log(name, age);
});
