from django.shortcuts import render, redirect
import random
def guess(request):
    if request.method == 'POST':
        secret_number = request.session.get('secret_number', None)
        guess = int(request.POST['guess'])
        attempts = request.session.get('attempts', 0)  # initialize attempts count to 0
        
        if secret_number is None:
            secret_number = random.randint(1, 100)
            request.session['secret_number'] = secret_number
            attempts = 0  # reset attempts count
        
        attempts += 1  # increment attempts count for each guess
        
        if guess < secret_number:
            message = "Too low! Guess again."
        elif guess > secret_number:
            message = "Too high! Guess again."
        else:
            message = f"Congratulations! You guessed the secret number ({secret_number}) in {attempts} attempts!"
            
            # Reset the game
            del request.session['secret_number']
            del request.session['attempts']
            
        # Update the attempts count in the session
        request.session['attempts'] = attempts
        
        return render(request, 'index.html', {'message': message})

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')
