const app = [
  { name: "ron", age: 20 },
  { name: "stephen", age: 23 },
  { name: "hey", age: 23 },
  { name: "heys", age: 23 },
];

app.map((item) => {
  console.log(item.name);
});
// console.log(item);

const data = app.filter((item) => {
  if (item.age == 20) {
    console.log(item.name);
  } else if (item.age == 23) {
    console.log(item.name);
  }
});
// console.log(data);
