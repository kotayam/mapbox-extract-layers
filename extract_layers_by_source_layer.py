#!/usr/bin/env python3
import os
import json

OUTPUT_DIR = "out/"

def load_source_layers(source_layer_file):
    with open(source_layer_file, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def extract_matching_layers(input_json, source_layer_file, output_json):
    target_src_layers = load_source_layers(source_layer_file)
    print(f"Log: layers to be extracted = {target_src_layers}")
    
    with open(input_json, 'r') as f:
        data = json.load(f)
    
    if "layers" in data and isinstance(data["layers"], list):
        filtered_layers = [layer for layer in data["layers"] if layer.get("source-layer") in target_src_layers or layer.get("type") == "background"]
        data["layers"] = filtered_layers
    else:
        print("Warning: No 'layers' list found in input JSON.")
        return

    os.makedirs(os.path.dirname(OUTPUT_DIR), exist_ok=True)

    output_path = OUTPUT_DIR + output_json

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Success: filtered JSON written to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract matching layers by source_layer.")
    parser.add_argument("input_json", help="Path to the input JSON file")
    parser.add_argument("source_layer_file", help="Path to the text file containing srouce layers to extract")
    parser.add_argument("output_json", help="Filename of the output JSON file")

    args = parser.parse_args()
    extract_matching_layers(args.input_json, args.source_layer_file, args.output_json)