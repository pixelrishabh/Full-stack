let n=prompt("enter the value of n");
n=Number.parseInt(n);
let fact=1;
for(let i=1;i<=n;i++){
    fact=fact*i;
}
console.log(fact)