document.getElementById('searchForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const ingredients = document.getElementById('ingredients').value;
    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ingredients})
        });
        const data = await response.text();
        window.location.href = `/search_results?data=${encodeURIComponent(data)}`;
    } catch (error) {
        console.error('Error:', error);
    }
});
