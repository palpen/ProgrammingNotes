# Notes on Go Programming Language

## Basic `go` tools commands
* To compile and run a script in a single step, do `go run myscript.go`

## Basic Go syntax

Run programs in main

```go
package main

import (
    "fmt"
)
 
func main() {
    fmt.Println("Hello, World!")
}
```

Functions

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

Loops

Three components:
1. init statement `i:=0` executed before first iteration
2. condition expression `i < 10` evaluated before every iteration
3. post statement `i++` executed at the end of every iteration

```
for i := 0; i < 10; i++ {
    fmt.Println("Hello, World!")
}
```

