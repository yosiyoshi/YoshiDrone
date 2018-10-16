# include "systemc.h"

SC_MODULE(adder)
{
	sc_in<int> a, b;
	sc_out<int> sum;

	void do_add()
	{
		sum = a + b;
	}

	SC_CTOR(adder)
	{
		SC_METHOD(do_add);
		sensitive << a << b;
	}
};

SC_MODULE(multiplier)
{
	sc_in<int> a, b;
	sc_out<int> sum;

	void do_multiple()
	{
		sum = a * b;
	}

	SC_CTOR(multiplier)
	{
		SC_METHOD(do_multiple);
		sensitive << a << b;
	}
}