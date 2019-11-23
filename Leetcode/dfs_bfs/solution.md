# Solution of DFS/BFS's Problems

### Medium

- \#200 Number of Islands

  Basic idea: DFS

  - Add margin to `grid`
  - For each element of value "1" in `grid`, DFS traverse through every adjacent element of value "1", then set them to "0" ,add 1 to `cnt`