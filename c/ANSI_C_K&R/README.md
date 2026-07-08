# An unnecessarily thorough guide to programming and everything hiding underneath it

## Foreword

This is not *true* K&R C. It borrows the spirit of that style — spare, direct, unadorned — but it isn't bound to its conventions. The code here may use C99 features, may not compile cleanly on every platform, and is written for the purpose of understanding rather than deployment. Do not ship it.

I wanted to teach in the spirit of K&R, but I also wanted to explain the things that book leaves for the reader to absorb on faith. This repository is my attempt to close that gap.

## My goal

### There will be no magic in this repository

If something happens, we ask why.
If a compiler accepts something, we ask why.
If an operating system behaves a certain way, we ask why.

If the answer is "because that's just how C works," we have not found the answer yet. That answer would be a placeholder for an explanation we haven't done the work to find.

### You will not find

- "Trust me."
- "Don't worry about this for now."
- "You'll understand it later."

If a concept appears, we stop and understand it. Only then do we continue.

My goal is to teach programming through a body of C code written in a style close to traditional K&R — because that style is the closest thing to language-neutral — while being far more verbose about *why* everything is the way it is. Nothing will stay unsaid. I will not assume you know anything about C, and I will not assume you know anything about programming at all. Every concept gets explained when it appears, and every explanation comes with an example.

The preface to *The C Programming Language* describes itself as a tutorial and reference, meant to get a new user productive quickly.

**I reject that framing entirely.**

Programming education today is obsessed with speed.

> "*Finish this tutorial in two hours.*"

> "*Learn C in one afternoon.*"

> "*Master pointers in ten minutes.*"

**No.**

If learning a language were merely memorizing syntax, every autocomplete plugin would already be a senior engineer.

Programming is understanding machines.

Programming is communicating with something so unimaginably literal that a single misplaced character changes reality.

Programming is building a precise model of how information moves, changes, occupies memory, and eventually becomes electricity flowing through silicon.

C merely strips away enough decoration that you can watch it happen.

### This repository is not about C

C is the microscope, not the specimen.

Programming isn't just syntax and language features — it's the concepts and principles underneath that make programs work at all. It's a skill built through practice, experimentation, and critical thinking, not through memorizing snippets or following tutorials. Learning to program means learning to *think* like a programmer: to communicate precisely with the machine. I think that's an art.

Knowing how a computer executes your code, allocates memory, manages resources, handles errors, and optimizes performance — that's what it takes to program well in *any* language. C is just the example I'm using to get there.

C is readable enough to teach with. It's low level, but not so low level that it stops being comfortable to work in. That's why it's the right tool for this.

And we will learn it **whole**.

## Final words

By the time you finish this repository, I can't promise you'll write perfect software.

We are not here to memorize C.

What I can promise is that "I copied this because Stack Overflow said so" will become physically painful.

We are here to become the sort of programmer who could have invented it themselves.

That is progress.

Enjoy.
