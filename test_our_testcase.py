import pytest
import sys
import os
import threading
from unittest.mock import MagicMock, patch

# We'll use a fixture to mock the imports that would cause side effects.
@pytest.fixture(autouse=True)
def mock_game_setup(monkeypatch):
    # Mocking os.system to prevent terminal clear commands
    monkeypatch.setattr('os.system', MagicMock())
    
    # Mocking pyttsx3 to prevent text-to-speech
    monkeypatch.setattr('pyttsx3.init', MagicMock())

    # Mocking playsound to prevent audio playback
    def mock_playsound(*args, **kwargs):
        pass # Do nothing
    monkeypatch.setattr('playsound.playsound', mock_playsound)

    def mock_thread_init(*args, **kwargs):
        return MagicMock()
    monkeypatch.setattr('threading.Thread', mock_thread_init)

    # We also need to mock the main loop's initial input
    monkeypatch.setattr('builtins.input', lambda prompt: 'TestPlayer')
    
# --- Test Helper Functions ---

def test_clear_screen_calls_os_system(monkeypatch):
    from main import clear_screen
    mock_system = MagicMock()
    monkeypatch.setattr('os.system', mock_system)
    
    # Test for Windows
    monkeypatch.setattr('os.name', 'nt')
    clear_screen()
    mock_system.assert_called_with('cls')
    
    # Test for Linux/macOS
    mock_system.reset_mock()
    monkeypatch.setattr('os.name', 'posix') # 'posix' is common for Linux/macOS
    clear_screen()
    mock_system.assert_called_with('clear')

# --- Test Blackjack Functions ---

def test_calculate_score_with_no_ace():
    """Tests the score calculation for a hand without an Ace."""
    from main import calculate_score
    assert calculate_score([10, 5, 2]) == 17
    assert calculate_score([8, 7]) == 15

def test_calculate_score_with_ace_as_11():
    """Tests the score calculation for an Ace counting as 11."""
    from main import calculate_score
    assert calculate_score([11, 7]) == 18

def test_calculate_score_with_ace_as_1():
    """Tests the score calculation where an Ace must be counted as 1 to avoid a bust."""
    from main import calculate_score
    assert calculate_score([11, 10, 5]) == 16
    assert calculate_score([11, 8, 4]) == 13

# --- Test Game Scenarios using Mocked Input ---

def test_blackjack_player_wins(monkeypatch, capsys):
    """Simulates a player winning a game of Blackjack."""
    from main import blackjack

    # Mock random.choice to give the player a winning hand and the dealer a losing hand.
    # Player's hand: [10, 9] -> stands.
    # Dealer's hand: [10, 6] -> hits -> [10, 6, 8] -> busts.
    cards_to_deal = [10, 9, 10, 6, 8]
    def mock_deal_card():
        return cards_to_deal.pop(0)

    monkeypatch.setattr('main.deal_card', mock_deal_card)
    
    # Mock input to simulate the player's choices
    # 's' for stand
    monkeypatch.setattr('builtins.input', lambda prompt: 's')
    
    # Run the function
    blackjack()
    
    # Capture the output
    captured = capsys.readouterr()
    assert "You win!" in captured.out
    assert "Sean clenches his fist and a vein bulges from his forehead" in captured.out

def test_blackjack_player_loses_to_dealer(monkeypatch, capsys):
    """Simulates a player losing to the dealer in Blackjack."""
    from main import blackjack

    # Mock random.choice to provide a hand where the dealer wins.
    # Player's hand: [10, 5] -> stands
    # Dealer's hand: [10, 8]
    cards_to_deal = [10, 5, 10, 8]
    def mock_deal_card():
        return cards_to_deal.pop(0)
        
    monkeypatch.setattr('main.deal_card', mock_deal_card)
    monkeypatch.setattr('builtins.input', lambda prompt: 's')
    
    blackjack()
    
    captured = capsys.readouterr()
    assert "Sean wins!" in captured.out

def test_blackjack_player_busts(monkeypatch, capsys):
    """Simulates a player busting and losing immediately."""
    from main import blackjack

    # Player hand: [10, 10] -> hits -> [10, 10, 5] -> busts
    # Dealer hand: [10, 8]
    cards_to_deal = [10, 10, 10, 8, 5]
    def mock_deal_card():
        return cards_to_deal.pop(0)

    monkeypatch.setattr('main.deal_card', mock_deal_card)
    # Player first hits, then busts, so their second input doesn't matter
    monkeypatch.setattr('builtins.input', lambda prompt: 'h')
    
    blackjack()

    captured = capsys.readouterr()
    assert "You busted! Sean wins." in captured.out
    
def test_library_func_finds_code(monkeypatch, capsys):
    from main import library_func_for_choice
    
    # Mock input to simulate the user's choices
    # 1. 'yes' to view the books
    # 2. 'god don't like ugly' to read the right book
    # 3. 'yes' to view the note
    user_inputs = ['yes', 'god don\'t like ugly', 'yes']
    def mock_input(prompt):
        return user_inputs.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)

    # Run the function
    library_func_for_choice()
    
    # Capture the output
    captured = capsys.readouterr()
    assert "51469" in captured.out

def test_exit_func_bad_ending_1(monkeypatch):
    from main import exit_func, exit_func_2
    
    # Mock input to choose 'yes' to confirm the exit
    monkeypatch.setattr('builtins.input', lambda prompt: 'yes')
    
    # We must mock time.sleep to not slow down the test
    monkeypatch.setattr('time.sleep', MagicMock())

    # We must mock the second `exit()` call
    monkeypatch.setattr('sys.exit', MagicMock())
    
    # The first exit function just prints a prompt and the second one takes the input
    exit_func()
    exit_func_2()
    
    # Check that sys.exit was called
    sys.exit.assert_called_once()
    
def test_boss_fight_win(monkeypatch, capsys):
    """
    Simulates the player winning the boss fight.
    """
    from main import boss_fight_func_for_choice
    
    # Mocking input to provide the correct code and fight choice
    user_inputs = ['51469', 'yes']
    def mock_input(prompt):
        return user_inputs.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    
    # Mocking random to ensure the player wins
    # user_attack_func always deals damage.
    # We need to make sure `mrs_brittany_health` is low from the start.
    monkeypatch.setattr('main.mrs_brittany_health', 1)
    
    # Set the user's health to a high value so they don't lose.
    monkeypatch.setattr('main.health_bar', 100)
    
    # Mock the various random functions called in the boss fight loop
    monkeypatch.setattr('main.random_user_attack', 'AI Code')
    monkeypatch.setattr('main.random_atack', 'Long, boring lesson')
    monkeypatch.setattr('main.user_number_attac_5', 5) # Ensure a one-hit kill
    
    # We must mock time.sleep to not slow down the test
    monkeypatch.setattr('time.sleep', MagicMock())
    
    # Run the boss fight
    boss_fight_func_for_choice(user_name='TestPlayer',
                               random_user_attack='AI Code',
                               mrs_brittany_health=1,
                               random_atack='Long, boring lesson',
                               boss_number_attac_1=1)

    captured = capsys.readouterr()
    assert "You win!" in captured.out
    assert "finally free from Base Camp." in captured.out

#If this shows it collected 10 things it works :)