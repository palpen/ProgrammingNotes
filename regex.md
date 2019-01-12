# Notes on Regular Expressions

1. Find some n number of digits in body of text
	* `\b\d{3}\b`
	* `\b`: anchor to perform "whole words only" search
		* It defines `word` in `\bword\b` as the word character
	* `\d` is for digits
	* `{3}` specifies the number of digits to match
