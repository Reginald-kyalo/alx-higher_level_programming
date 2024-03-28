#!/usr/bin/node

let num = 0;
let num2 = 0;
let i = 0;
let j = 2;

if (process.argv.length === 0 || process.argv.length === 1)
{
	console.log(0);
}
else
{
	while(i < process.argv.length)
	{
		if (num < process.argv[j])
		{
			num = process.argv[j];
		}
		i++;
		j++;
	}
	i = 0;
	j = 0;
	while (i < process.argv.length)
	{
		if (num2 < process.argv[j] && num2 < num)
		{
			num2 = process.argv[j];
		}
		i++;
		j++;
	}
	console.log(num2);
}
