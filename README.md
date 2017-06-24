# pupd

Simple web service on top of [pup](https://github.com/ericchiang/pup)

## Example

There's a running instance hosted on dom.now.sh

You can use the same [syntax](https://github.com/ericchiang/pup#examples), except it always returns JSON.

`https://dom.now.sh/parse?url=<URL>&selector=<CSS selector>`

## Notes
Actually `selector` argument is sent as any parameter to `pup` binary (I didn't bother to parse it)

Despite I haven't taken a look at `pup` code, believing in its parsing job, it might be better to write this in Go using it as a module, I was just testing Python 3.5+ asyncio libraries