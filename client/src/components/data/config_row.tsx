type ConfigRowProps = {
    title: string,
    titleWidth?: number,
    component?: JSX.Element,
}

function ConfigRow(props: ConfigRowProps) {
    const { title, titleWidth, component } = props;
    return (
        <div className="flex flex-row justify-start items-center w-full">
            <span className={`text-[#A1ACAB] font-semibold text-[14px] w-[${titleWidth ?? 200}px] flex justify-start`}>{title}</span>
            <div className="flex-grow flex justify-start">
                {component}
            </div>

        </div>
    )
}
export default ConfigRow;