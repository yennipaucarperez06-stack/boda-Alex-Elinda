document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('confirmationModal');
    const btn = document.getElementById('rsvpBtn');
    const span = document.getElementsByClassName('close')[0];


    // When user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }

      // Close modal with animation

    
});