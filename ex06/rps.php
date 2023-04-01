<?php
	// Colors
	$red = "\033[0;31m";
	$green = "\033[0;32m";
	$yellow = "\033[0;33m";
	$blue = "\033[0;34m";
	$purple = "\033[0;35m";
	$cyan = "\033[0;36m";

	$bold_red = "\033[1;31m";
	$bold_green = "\033[1;32m";
	$bold_yellow = "\033[1;33m";
	$bold_blue = "\033[1;34m";
	$bold_purple = "\033[1;35m";
	$bold_cyan = "\033[1;36m";

	$reset = "\033[0m";

	$choices = array('rock', 'paper', 'scissors');
	
	$user_score = 0;
	$computer_score = 0;
	
	system('clear');
	echo $blue . "Welcome to Rock, Paper, Scissors!\n" . $reset;
	while (true) {
		$computer = $choices[rand(0,2)];
		while (true) {
			echo $cyan . "Enter your choice ($yellow 👊 rock$reset, $purple 📄 paper$reset, $red ✂️  scissors$reset): ";
			$user = trim(fgets(STDIN));
			if (in_array($user, $choices)) {
				break;
			}
			echo $red . "Invalid choice. Try again.\n" . $reset;
		}
		echo "\n";
		switch ($user) {
			case 'rock':
				if ($computer == 'rock') {
					echo $bold_yellow . "🤝 Tie! The computer chose rock.\n" . $reset;
				} elseif ($computer == 'paper') {
					echo $bold_red . "😔 Sorry, you lost. The computer chose paper.\n" . $reset;
					$computer_score++;
				} else {
					echo $bold_green . "🎉 Congratulations! You won! The computer chose scissors.\n" . $reset;
					$user_score++;
				}
				break;
			case 'paper':
				if ($computer == 'rock') {
					echo $bold_green . "🎉 Congratulations! You won! The computer chose rock.\n" . $reset;
					$user_score++;
				} elseif ($computer == 'paper') {
					echo $bold_yellow . "🤝 Tie! The computer chose paper.\n" . $reset;
				} else {
					echo $$bold_red . "😔 Sorry, you lost. The computer chose scissors.\n" . $reset;
					$computer_score++;
				}
				break;
			default:
				if ($computer == 'rock') {
					echo $bold_red . "😔 Sorry, you lost. The computer chose rock.\n" . $reset;
					$computer_score++;
				} elseif ($computer == 'paper') {
					echo $bold_green . "🎉 Congratulations! You won! The computer chose paper.\n" . $reset;
					$user_score++;
				} else {
					echo $bold_yellow . "🤝 Tie! The computer chose scissors.\n" . $reset;
				}
				break;
		}
		echo $bold_purple . "Score: You $user_score, Computer $computer_score\n\n" . $reset;
		while (true) {
			echo $cyan . "Play again? ($green y $reset/$red n $reset): ";
			$play_again = trim(fgets(STDIN));
			if ($play_again == 'y' || $play_again == 'n') {
				if ($play_again == 'y') {
					system('clear');
				}
				break;
			}
			echo $red . "Invalid choice. Try again.\n" . $reset;
		}
		if ($play_again == 'n') {
			break;
		}
	}
	echo $cyan . "Thanks for playing!\n" . $reset;
?>
