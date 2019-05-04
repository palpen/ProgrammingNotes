# Notes on Go Programming Language

## Basic `go` tools commands
* To compile and run a script in a single step, do `go run myscript.go`

## Basic Go syntax

* Run programs in main

```go
package main

import (
    "fmt"
)
 
func main() {
    fmt.Println("Hello, World!")
}
```

__Functions__

```go

package main

import "fmt"

func add(x int, y int) int {
    return x + y
}

func main() {
    fmt.Println(add(42, 13))
}
```

__Loops__

Three components:
1. init statement `i:=0` executed before first iteration
2. condition expression `i < 10` evaluated before every iteration
3. post statement `i++` executed at the end of every iteration

```go
for i := 0; i < 10; i++ {
    fmt.Println("Hello, World!")
}
```

__Slice__

```go
// initialize with some values
myslice := []int{}

// initialize with nil value
var myslice []int
```

Appending slices together

```golang
s1 := []int{1, 3, 5}
s2 := []int{2, 4, 6}
s3 := []int{}
s3 = append(s1, s2...) \\ s3 == [1,3,5,2,4,6]
```

or just the first two elements of `s2`

```golang
s3 := []int{}
s3 = append(s1, s2[0:2]...) \\ s3 == [1,3,5,2,1]
```

__Iterating through a slice__

```go
\\ i gives the index, v the value
for i, v := range myslice {
    fmt.Println(i, v)
}
```

## Read a text file into a slice

Read in data that looks like this

```
12
43
23
55
```

into a slice of strings

```golang

import (
	"os"
	"log"
	"bufio"
)

func ReadText(textfile_name string) []string {

	file, err := os.Open(textfile_name)

	if err != nil {
		log.Fatalf("Failed to open file: %s", err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var txtlines []string

	for scanner.Scan() {

		txtlines = append(txtlines, scanner.Text())
	}

	file.Close()

	return txtlines
}
```
