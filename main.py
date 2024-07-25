from classes import ProcessNode, UpTreeCompetition


# create a function to iterate the message generation and competition for t time steps
def run_simulation(num_nodes, time_steps, verbose=True):
    # Create the process nodes
    print('Number of Nodes:', num_nodes)
    process_nodes = [ProcessNode(i) for i in range(num_nodes)]
    print()

    # Set the first message for each node
    for node in process_nodes:
        node.set_first_message()

    # Create the up-tree competition
    up_tree_competition = UpTreeCompetition()

    # Run the simulation for t time steps
    for i in range(time_steps):
        if verbose:
            # Show the messages for each node
            print('Time Step:', i)
            for node in process_nodes:
                print(node.message)
            print()

        # Add the messages to the up-tree competition
        for node in process_nodes:
            up_tree_competition.add_message(node.message)
        
        # Get the winner of the competition and clear the messages
        winner = up_tree_competition.get_winner()

        # show the contents of the winner
        print('Winner:', winner)
        print()
        
        up_tree_competition.clear()

        # Update the nodes based on the winner
        for node in process_nodes:
            print('Previous Message:', node.message)
            node.update_node(winner)
            print('Updated Message:', node.message)
            print()
    return


def main():
    # Set the number of nodes and the time steps for the simulation
    num_nodes = 3
    time_steps = 5

    # Run the simulation
    run_simulation(num_nodes, time_steps)
    return

if __name__ == '__main__':
    main()