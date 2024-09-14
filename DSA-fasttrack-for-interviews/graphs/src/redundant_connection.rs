struct UnionFind {
    parents: Vec<usize>,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        UnionFind {
            parents: {
                let mut parents: Vec<usize> = vec![0; size + 1];
                for i in 0..size {
                    parents[i] = i;
                }
                parents
            },
        }
    }

    fn union(&mut self, a: usize, b: usize) {
        let pa = self.find(a);
        let pb = self.find(b);
        if pa != pb {
            self.parents[pa] = pb;
        }
    }

    fn find(&mut self, a: usize) -> usize {
        if self.parents[a] == a {
            return a;
        }
        let parent = self.find(self.parents[a]);
        self.parents[a] = parent;
        parent
    }
}

pub fn run(edges: Vec<Vec<i32>>) -> Vec<i32> {
    let mut uf: UnionFind = UnionFind::new(edges.len());
    for e in edges {
        if uf.find(e[0] as usize) == uf.find(e[1] as usize) {
            return e;
        }
        uf.union(e[0] as usize, e[1] as usize);
    }
    Vec::new()
}