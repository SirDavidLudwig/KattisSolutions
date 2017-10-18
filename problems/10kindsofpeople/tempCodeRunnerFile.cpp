if (next = map[current->y][current->x-1]) {
				if (next->group == -1 && next->type == current->type)
					search.push(next);
			}
			if (next = map[current->y][current->x+1]) {
				if (next->group == -1 && next->type == current->type)
					search.push(next);
			}