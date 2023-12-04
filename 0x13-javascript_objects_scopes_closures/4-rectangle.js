#!/usr/bin/node
/**
 * Represents a rectangle
 */
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
		this.width = w;
		this.height = h;
		}
	}

	print() {
		const shape = 'X';
		for (let i = 0; i < this.height; i++) {
			console.log(shape.repeat(this.width));
		}
	}

	rotate() {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
