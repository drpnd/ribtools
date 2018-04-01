# Routing Information Base toolset

## Split routing table

    $ python scripts/split.py --input-file=<prefix file> --split-mode=<mode>

* Mode 2: Each prefix that is no longer than {\tt /24}, {\tt /20}, and {\tt /16} is split into two, four, and eight prefixes, respectively.
* Mode 4: Each prefix that is no longer than {\tt /24}, {\tt /23}, {\tt /20}, and {\tt /16} is split into two, four, eight, and sixteen prefixes, respectively.
