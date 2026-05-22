"""
Audio Processing Module
Handles audio analysis and frequency extraction.

This module will be used for server-side audio processing in future versions.
Currently, all audio processing happens in the browser via Web Audio API.
"""

import numpy as np


class AudioProcessor:
    """Processes audio data and extracts frequency information"""
    
    def __init__(self, sample_rate=44100, fft_size=4096):
        """
        Initialize audio processor
        
        Args:
            sample_rate: Audio sample rate in Hz (default: 44100)
            fft_size: FFT window size (default: 4096)
        """
        self.sample_rate = sample_rate
        self.fft_size = fft_size
        self.freq_resolution = sample_rate / fft_size
    
    def apply_window(self, audio_data):
        """Apply Hann window to reduce spectral leakage"""
        window = np.hanning(len(audio_data))
        return audio_data * window
    
    def compute_fft(self, audio_data):
        """
        Compute FFT of audio data
        
        Args:
            audio_data: Audio samples (numpy array)
        
        Returns:
            Magnitude spectrum
        """
        windowed = self.apply_window(audio_data)
        fft_output = np.fft.fft(windowed, n=self.fft_size)
        magnitude = np.abs(fft_output[:len(fft_output)//2])
        return magnitude
    
    def find_peak_frequency(self, magnitude_spectrum):
        """
        Find the peak frequency in magnitude spectrum
        
        Args:
            magnitude_spectrum: FFT magnitude output
        
        Returns:
            Tuple of (frequency in Hz, normalized magnitude)
        """
        peak_bin = np.argmax(magnitude_spectrum)
        peak_magnitude = magnitude_spectrum[peak_bin]
        frequency = peak_bin * self.freq_resolution
        normalized = min(peak_magnitude / 128, 1.0)
        
        return frequency, normalized


# Example usage:
if __name__ == '__main__':
    import math
    
    # Create a test tone (440 Hz sine wave)
    processor = AudioProcessor()
    duration = 0.1  # 100ms
    samples = int(processor.sample_rate * duration)
    t = np.linspace(0, duration, samples)
    
    # Generate 440 Hz sine wave
    tone = np.sin(2 * np.pi * 440 * t).astype(np.float32)
    
    # Process it
    magnitude = processor.compute_fft(tone)
    freq, mag = processor.find_peak_frequency(magnitude)
    
    print(f"Generated: 440 Hz sine wave")
    print(f"Detected: {freq:.1f} Hz")
    print(f"Magnitude: {mag:.2f}")
