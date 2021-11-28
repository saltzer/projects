fn main() {
	let mut a: f32 = 0.;
	let mut b: f32 = a;
	print!("\x1b[2J");
	loop {
		let (mut r, mut z, mut j, sc) = ([' '; 1760], [0.; 1760], 0., f32::sin_cos);
        while j < 6.28 {
			let mut i = 0.;
			while i < 6.28 {
				let ((c, l), (f, d), (e, g), (n, m)) = (sc(i), sc(j), sc(a), sc(b));
				let h = d + 2.;
				let (p, t) = (1. / (c * h * e + f * g + 5.), c * h * g - f * e);
				let (x, y) = ((40. + 30. * p * (l * h * m - t * n)) as usize, (12. + 15. * p * (l * h * n + t * m)) as usize);
				let o = x + 80 * y;
				let q = (8. * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)) as usize;
				if 22 > y && y > 0 && x > 0 && 80 > x && p > z[o] {
					z[o] = p;
					r[o] = b".,-~:;=!*#$@"[q.max(0)] as char;
				}
				i += 0.02;
			}
			j += 0.08;
		}
		print!("\x1b[H");
		for k in 0..1761 {
			print!("{}", if k % 80 != 0 {r[k]} else {'\n'});
			a += 4e-5;
			b += 2e-5;
		}
		std::thread::sleep(std::time::Duration::from_millis(30));
	}
}
