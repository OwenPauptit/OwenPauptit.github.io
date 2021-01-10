class Blob
{
    constructor(x,y)
    {
        this.pos = new Vector(x,y);
        this.vel = new Vector(Math.random()*2-1,Math.random()*2-1);
        this.vel = Vector.Scale(this.vel,Math.random()*3+5)
        this.r = 40;
    }

    update(width, height)
    {
        this.pos = Vector.Add(this.pos,this.vel);

        if (this.pos.x > width || this.pos.x < 0)
        {
            this.vel.x *= -1;
        }
        if (this.pos.y > height || this.pos.y < 0)
        {
            this.vel.y *= -1;
        }
    }

    draw(ctx)
    {
        ctx.strokeStyle="white";
        ctx.beginPath();
        ctx.arc(this.pos.x,this.pos.y,this.r,0,Math.PI*2,true);
        ctx.stroke();
    }
}