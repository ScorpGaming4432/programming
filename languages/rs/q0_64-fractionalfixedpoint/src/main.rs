use std::ops::{Add, Div, Mul, Sub};

/// A 64-bit unsigned fixed-point fraction in the range `[0, 1)`.
///
/// `UFrac64` stores fractional values as an unsigned 64-bit integer where the
/// represented value is `raw / 2^64`.
///
/// This type is useful for high-precision fractional computations when values
/// are known to be non-negative and strictly less than 1.
struct UFrac64(u64);

impl UFrac64 {
    /// Creates a `UFrac64` from an `f64` value in the range `[0, 1)`.
    ///
    /// The input is scaled by `2^64` and rounded to the nearest representable
    /// fixed-point value.
    ///
    /// # Panics
    ///
    /// Panics if `value` is outside the valid range `[0, 1)`.
    pub fn from_f64(value: f64) -> Self {
        assert!(0.0 <= value && value < 1.0, "Value must be in the range [0, 1)");
        UFrac64((value * 2.0_f64.powf(64.0)).round() as u64)
    }

    /// Converts the fixed-point value back to `f64`.
    ///
    /// The stored raw bits are divided by `2^64` to recover the original
    /// fractional magnitude.
    pub fn to_f64(&self) -> f64 {
        self.0 as f64 / (2.0_f64.powf(64.0)) as f64
    }
}

impl Add for UFrac64 {
    type Output = Self;

    /// Adds two `UFrac64` values using the underlying fixed-point representation.
    ///
    /// This performs raw integer addition on the internal `u64` fields.
    fn add(self, other: Self) -> Self {
        UFrac64(self.0 + other.0)
    }

    // fn add(self, other: IFrac64) -> Self {
    //     UFrac64(self.0 + other.0 as u64)
    // }
}

impl Sub for UFrac64 {
    type Output = Self;

    /// Subtracts one `UFrac64` from another using the underlying fixed-point representation.
    fn sub(self, other: Self) -> Self {
        UFrac64(self.0 - other.0)
    }
}

impl Mul for UFrac64 {
    type Output = Self;

    /// Multiplies two `UFrac64` values and returns their fixed-point product.
    ///
    /// The multiplication is performed in `u128` and shifted right by 64 bits
    /// to keep the result in the same fixed-point format.
    fn mul(self, other: Self) -> Self {
        let product = (self.0 as u128 * other.0 as u128) >> 64;
        UFrac64(product as u64)
    }
}

impl Div for UFrac64 {
    type Output = Self;

    /// Divides one `UFrac64` by another and returns the fixed-point quotient.
    ///
    /// The numerator is promoted to `u128` before division to preserve precision.
    fn div(self, rhs: Self) -> Self::Output {
        let dividend = (self.0 as u128) << 64;
        let quotient = dividend / rhs.0 as u128;
        UFrac64(quotient as u64)
    }
}

/// A 64-bit signed fixed-point fraction in the range `(-1, 1)`.
///
/// Positive values are encoded directly as a signed integer scaled by `2^63`.
/// Negative values are encoded using a bitwise complement of the absolute
/// magnitude, which preserves distinct positive and negative zero values.
struct IFrac64(i64);

// impl IFrac64 {
//     pub fn from_f64(value: f64) -> Self {
//         let scaled: i64 = (value * (1_i64 << 63) as f64).round() as i64;
//         IFrac64(scaled)   
//     }

//     pub fn to_f64(&self) -> f64 {
//         self.0 as f64 / (1_i64 << 63) as f64
//     }
// }


/// IFrac64 is a structure that represents a signed fractional number in the range (-1, 1) using a 64-bit integer. It is designed to allow for precise representation of fractional values, including negative ones, while maintaining a compact memory footprint. The most significant bit of the 64-bit integer is used to indicate the sign of the number, while the remaining 63 bits represent the fractional part. This structure is particularly useful for mathematical computations that require high precision and the ability to represent values close to zero in both positive and negative directions, such as limits and derivatives in calculus.
impl IFrac64 {

    /// Creates an `IFrac64` from an `f64` in the range `(-1, 1)`.
    ///
    /// Positive values are encoded directly as `value * 2^63`. Negative values are
    /// encoded as the bitwise complement of the absolute scaled magnitude.
    ///
    /// This encoding preserves distinct positive and negative zero representations.
    ///
    /// # Panics
    ///
    /// Panics if `value` is not strictly between `-1` and `1`.
    pub fn from_f64(value: f64) -> Self {
        assert!(-1.0 < value && value < 1.0, "Value must be in the range (-1, 1)");
        
        if value >= 0.0 {
            // Positive value: scale by 2^63
            let scaled = (value * 2.0_f64.powi(63)).round() as i64;
            IFrac64(scaled)
        } else {
            // Negative value: apply NOT operation on the absolute value's representation
            let abs_value = -value;
            let scaled = (abs_value * 2.0_f64.powi(63)).round() as u64;
            let negated = !scaled as i64;
            IFrac64(negated)
        }
    }

    /// Converts this `IFrac64` back into an `f64`.
    ///
    /// Positive values decode directly. Negative values recover the absolute
    /// magnitude by applying bitwise complement to the stored representation.
    pub fn to_f64(&self) -> f64 {
        if self.0 >= 0 {
            // Positive value: direct conversion
            self.0 as f64 / 2.0_f64.powi(63)
        } else {
            // Negative value: apply NOT to recover the absolute value's representation
            let positive = !(self.0 as u64);
            -(positive as f64 / 2.0_f64.powi(63))
        }
    }
}

impl Add for IFrac64 {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        let result = self.0 + other.0;
        assert!(-1 <= result && result <= 1, "Result must be between -1 and 1");
        IFrac64(self.0 + other.0)
    }

    // fn add(self, other: IFrac64) -> Self {
    //     UFrac64(self.0 + other.0 as u64)
    // }
}

impl Sub for IFrac64 {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        let result = self.0 - other.0;
        assert!(-1 <= result && result <= 1, "Result must be between -1 and 1");
        IFrac64(self.0 - other.0)
    }
    
}

impl Mul for IFrac64 {
    type Output = Self;

    fn mul(self, other: Self) -> Self {
        let product = (self.0 as i128 * other.0 as i128) >> 64;
        IFrac64(product as i64)
    }
    
}

// impl Div for IFrac64 {
//     type Output = Self;

//     /// Doesn't handle division, since anything less than zero over anything else is going to be more than one.
//     /// Wraps back to floating point division for now, since this is just a proof of concept.
//     fn div(self, rhs: Self) {
//         return self.to_f64() / rhs.to_f64();
//     }
// }



fn main() {
    let a: UFrac64 = UFrac64::from_f64(0.5);
    let b: UFrac64 = UFrac64::from_f64(0.25);
    println!("{} / {} = {}\n", a.to_f64(), b.to_f64(), (a/b).to_f64());

    let c: IFrac64 = IFrac64::from_f64(-0.5);
    let d: IFrac64 = IFrac64::from_f64(0.25);
    // println!("{} / {} = {}\n", c.to_f64(), d.to_f64(), (c/d).to_f64());
    println!("{} * {} = {}\n", c.to_f64(), d.to_f64(), (c.to_f64() * d.to_f64()));

    println!("Hello, world!");
}
