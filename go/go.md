# Notes on Go Programming Language

* To compile and run a script in a single step, do `go run myscript.go`

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