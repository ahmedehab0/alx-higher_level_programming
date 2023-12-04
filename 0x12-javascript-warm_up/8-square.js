#!/usr/bin/node

const shape = 'X';
const num = parseInt(process.argv[2]);

if (!isNaN(num)){
	for (let i = num; i > 0; i--)
	{
		console.log(shape.repeat(num));
	}
} else{
	console.log("Missing size");
}
