"""
Pitch Detection Module
Analyzes frequency data and calculates tuning information.

This module will handle server-side pitch detection in future versions.
Currently, pitch detection happens in the browser via Web Audio API.
"""

import math


class PitchDetector:
    """Detects pitch from frequency data"""
    
    def __init__(self):
        """Initialize pitch detector"""
        self.string_frequencies = {
            'E2': 82.41,
            'A': 110.00,
            'D': 146.83,
            'G': 196.00,
            'B': 246.94,
            'E4': 329.63
        }
    
    def calculate_cents(self, detected_freq, target_freq):
        """
        Calculate cents deviation from target frequency
        
        Formula: 1200 * log2(detected / target)
        
        Args:
            detected_freq: Detected frequency in Hz
            target_freq: Target frequency in Hz
        
        Returns:
            Cents deviation
        """
        if detected_freq <= 0 or target_freq <= 0:
            return 0.0
        
        return 1200 * math.log2(detected_freq / target_freq)
    
    def get_status(self, cents):
        """Get tuning status (in-tune, flat, sharp)"""
        if abs(cents) < 5:
            return {'status': 'in-tune', 'message': '✓ In tune!'}
        elif cents < -5:
            return {'status': 'flat', 'message': '↑ Tune up'}
        else:
            return {'status': 'sharp', 'message': '↓ Tune down'}


# Example usage:
if __name__ == '__main__':
    detector = PitchDetector()
    
    # Test: Detect E string (82.41 Hz)
    detected = 82.5
    target = 82.41
    cents = detector.calculate_cents(detected, target)
    status = detector.get_status(cents)
    
    print(f"Detected: {detected} Hz")
    print(f"Target: {target} Hz")
    print(f"Deviation: {cents:.1f} cents")
    print(f"Status: {status['message']}")
