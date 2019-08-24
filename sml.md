# Notes on Standard ML

## Resolving various installation issues

* If you get `sml: unable to determine architecture/operating system` on a MacOS, follow instructions [here](https://stackoverflow.com/a/14411001). For MacOS Mojave, add

    `18*) OPSYS=darwin; HEAP_OPSYS=darwin ;; # MacOS X 10.14 Mojave`

* If libraries fail to autoload and you get this error:

```
unexpected exception (bug?) in SML/NJ: Io [Io: openIn failed on "/Users/jhr/Work/smlnj/osx-dist/smlnj.dst/sml.boot.x86-unix/smlnj/basis/.cm/x86-unix/basis.cm", No such file or directory]
 raised at: Basis/Implementation/IO/bin-io-fn.sml:617.25-617.71
         ../cm/util/safeio.sml:30.11
         ../compiler/TopLevel/interact/evalloop.sml:42.54
```

Either reinstall sml using Homebrew: `brew update; brew install smlnj` or do [this](https://stackoverflow.com/a/54224742). Namely, add `export SMLNJ_HOME=/usr/local/smlnj/` to start-up script of your shell (e.g. `.zshrc`)
