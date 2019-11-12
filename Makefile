FC = gfortran
FCFLAGS = -fPIC -std=f2003 -fall-intrinsics
LDFLAGS = -shared

LIBD3 = pydftd3/libdftd3.so

all: $(LIBD3)

vpath % src:lib/lib

.PHONY: clean distclean


OBJS  = api.o common.o core.o pars.o sizes.o c_wrapper.o

$(LIBD3): $(OBJS)
	$(FC) ${LDFLAGS} -o $(LIBD3) $(OBJS) 


clean:
	rm -f *.o

distclean: clean
	rm -f *.mod $(LIBD3)


%.o: %.f90
	$(FC) $(FCFLAGS) -c $< -o $@


# Dependencies
api.o: common.o core.o sizes.o
common.o:
core.o: common.o pars.o sizes.o
pars.o: common.o sizes.o
sizes.o:
c_wrapper.o: api.o
