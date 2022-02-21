tmux \
new-session "python3 read.py ; read" \; \
split-window "python3 send.py ; read" \; \
select-layout even-vertical
