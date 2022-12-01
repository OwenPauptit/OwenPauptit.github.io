const g = 1;

class DoublePendulum
{

    constructor(m1,m2,r1,r2,a1,a2)
    {
        this.r1 = r1;
        this.r2 = r2;
        this.m1 = m1;
        this.m2 = m2;
        this.a1 = a1;
        this.a2 = a2;
        this.a1_v = 0;
        this.a2_v = 0;
        this.a1_a = 0;
        this.a2_a = 0;
        this.tail = []
    }

    update()
    {

        var m1 = this.m1;
        var m2 = this.m2;
        var a1 = this.a1;
        var a2 = this.a2;
        var a1_v = this.a1_v;
        var a2_v = this.a2_v;
        var r1 = this.r1;
        var r2 = this.r2;



        var num1 = - g * (2 * m1 + m2) * Math.sin(a1)
        var num2 = - m2 * g * Math.sin(a1 - 2 * a2)
        var num3 = - 2 * Math.sin(a1 - a2) * m2
        var num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * Math.cos(a1 - a2);
        var den = r1 * (2 * m1 + m2 - m2 * Math.cos(2 * a1 - 2 * a2))
        this.a1_a = (num1 + num2 + num3*num4) / den;

        num1 = 2 * Math.sin(a1 - a2);
        num2 = a1_v * a1_v * r1 * (m1 + m2);
        num3 = g * (m1 + m2) * Math.cos(a1);
        num4 = a2_v * a2_v * r2 * m2 * Math.cos(a1 - a2);
        var den = r2 * (2 * m1 + m2 - m2 * Math.cos(2 * a1 - 2 * a2))
        this.a2_a = (num1 * (num2 + num3 + num4)) / den;


        this.a1_v += this.a1_a;
        this.a2_v += this.a2_a;


        this.a1 += this.a1_v;
        this.a2 += this.a2_v;
    }

    draw(ctx, pendulumColour="white", tailColour="#aaaaaa")
    {

        var x1 = this.r1 * Math.sin(this.a1);
        var y1 = this.r1 * Math.cos(this.a1);
        var x2 = x1 + this.r2 * Math.sin(this.a2);
        var y2 = y1 + this.r2 * Math.cos(this.a2);
        this.tail.push([x2,y2]);
        if (this.tail.length > 1200)
        {
            this.tail.shift();
        }
        ctx.strokeStyle = tailColour;
        ctx.lineWidth = 1;
        for (var i = 1; i < this.tail.length; i++)
        {
            ctx.beginPath();
            ctx.moveTo(this.tail[i-1][0], this.tail[i-1][1]);
            ctx.lineTo(this.tail[i][0], this.tail[i][1]);
            ctx.stroke();
        }
        ctx.lineWidth = 2;
        ctx.fillStyle = pendulumColour;
        ctx.strokeStyle = pendulumColour;
        ctx.beginPath();
        ctx.arc(0, 0, 10, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(x1, y1, this.m1, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(x2, y2, this.m2, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.lineTo(x1,y1);
        ctx.lineTo(x2,y2);
        ctx.stroke();

    }
}