# Getting Started with Scala

## How to quickly run Scala code
1. Write your script in an object (Hello in this case) that extends the App trait and save it as a `Hello.scala` file
```scala
object Hello extends App {
    println("Hello, World")
}
```
2. In the command line, compile your code with `scalac Hello.scala`
3. When it finishes compiling, run it with `scala Hello`

The purpose of extending `App` trait is to avoid having to write your own `main` method. [It quickly turns objects into executable programs.](https://www.scala-lang.org/api/2.10.3/index.html#scala.Application) It apparently has [several drawbacks](https://stackoverflow.com/questions/24437423/in-scala-should-i-use-the-app-trait), the description of which is beyond my understanding at this point.

One could, as a consequence, just define a `main` method as follows

```scala
object Hello {
  def main(args: Array[String]) {
    println("Hello, world!")
  }
}
```
