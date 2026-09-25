function downloadGame() {
	fetch('https://raw.githubusercontent.com/Tommy3541/lkjhg/refs/heads/main/hra.py')
		.then(response => response.blob())
		.then(file => {
			const link = document.createElement('a');
			link.href = URL.createObjectURL(file);
			link.download = 'hra.py';
			link.click();
		});
}
