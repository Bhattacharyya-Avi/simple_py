import pytest
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10, 10) == 0
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(4, 5) == 20
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-3, 4) == -12
    
    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(10, 2) == 100


def test_main_function(capsys):
    """Test the main function output."""
    from calculator import main
    main()
    captured = capsys.readouterr()
    assert "Calculator Demo:" in captured.out
    assert "5 + 3 = 8" in captured.out


if __name__ == "__main__":
    pytest.main([__file__])