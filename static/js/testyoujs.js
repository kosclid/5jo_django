function lidi (inst) {
    
    if (!inst.status) {inst.status = 0;}

    
    inst.hWrap.classList.add("lidiWrap");

    inst.hUp = document.createElement("div");
    inst.hDown = document.createElement("div");
    inst.hUp.className = "lidiUp";
    inst.hDown.className = "lidiDown";


    if (inst.status ==1) {inst.hUp.classList.add("set");}
    if (inst.status ==-1) {inst.hDown.classList.add("set");}
    inst.hWrap.appendChild(inst.hUp);
    inst.hWrap.appendChild(inst.hDown);

    inst.updown = (up) => {
        if (up) {
            inst.status = inst.status == 1 ? 0: 1;
        }
        else {
            inst.status = inst.status == -1 ? 0: -1;
        }

        if (inst.status ==1) {
            inst.hUp.classList.add("set");
            inst.hDown.classList.remove("set");
        } else if (inst.status ==-1) {
            inst.hUp.classList.remove("set");
            inst.hDown.classList.add("set");
        } else {
            inst.hUp.classList.remove("set");
            inst.hDown.classList.remove("set");
        }

        inst.change(inst.status);
    };

    inst.enable = () => {
        inst.hUp.onclick = () => { inst.updown(true); };
        inst.hDown.onclick = () => { inst.updown(false); };
    }
    inst.disable = () => {
        inst.hUp.onclick = "";
        inst.hDown.onclick = "";
    }
    inst.enable();
}