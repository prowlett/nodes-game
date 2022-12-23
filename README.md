# nodes game tree search

For demo purposes, rather than a serious game. 

- `nodes-description.tex` (output as `nodes-description.pdf` and `nodes-description.png`) is a description of the game.
- `nodes.py` is a program I claim searches the game tree for this game.
- `nodes-outputversion.py` is `nodes.py` with added code to output game trees as LaTeX files using the `forest` package. So `nodes-n-game-tree.tex` is the game on a line of n nodes and is output as `nodes-n-game-tree.pdf`. Included are n=1,...,5 versions. The n=6 version would not run through pdflatex (`! Dimension too large.`).

The question is how would I go about proving that `nodes.py` is doing what I claim it is doing? I asked this [on Mathstodon here](https://mathstodon.xyz/@peterrowlett/109562627259578520).
