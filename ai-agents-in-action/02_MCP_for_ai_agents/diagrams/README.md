# Diagrams

GitHub doesn't render Mermaid inside `.ipynb` files, so the notebook shows these as SVG images. The `.mmd` files are the editable source.

To change a diagram, edit its `.mmd` file, then re-render from this folder:

```powershell
npx -y @mermaid-js/mermaid-cli@12.2.0 -c mermaid-config.json -b white -i research_agent.mmd -o research_agent.svg
npx -y @mermaid-js/mermaid-cli@12.2.0 -c mermaid-config.json -b white -i json_rpc_workflow.mmd -o json_rpc_workflow.svg
```

`mermaid-config.json` turns off HTML labels so the text is plain SVG, which displays correctly when GitHub shows the file as an image.
