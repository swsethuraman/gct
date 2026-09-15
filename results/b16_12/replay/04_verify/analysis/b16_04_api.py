from flint import fmpq_mpoly_ctx, fmpq
ctx=fmpq_mpoly_ctx.get(('x','y'))
x,y=ctx.gens()
print(type(x),[s for s in dir(x) if not s.startswith('_')])
print((x+y).to_dict())
print(ctx.from_dict({(1,0):fmpq(1,2)}))
print(x.compose.__doc__)
print(x.subs.__doc__)
