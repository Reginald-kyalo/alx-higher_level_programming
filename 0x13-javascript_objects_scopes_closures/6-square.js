#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle
{
	constructor(length)
	{
		super(length, length);
	}

	charPrint(c)
	{
		if (c === undefined)
		{
			super.print();
		}
		else
		{
			for (let i = 0; i < this.width; i++)
			{
				console.log(c.repeat(this.width).trim());
			}
		}
	}
}
module.exports = Square;
